import asyncio
from threading import Thread
import queue
import os
import socketio
from aiohttp import web

INDEX_HTML = """
<!DOCTYPE HTML>
<html>
<head>
    <title>PhasmoCompanion Overlay Server</title>
    <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.2/socket.io.min.js"></script>
</head>
<body>
    <h1>PhasmoCompanion Overlay Server</h1>
    Use this page as a template to create some interesting overlays. When data is changed in PhasmoCompanion, the updates are reflected here in the javascript function "on_update".
    <h2>Status:</h2>
    <div id="status">Disconnected</div>
    <p>
    <h2>Current Data:</h2>
    <p>
    <div><pre id="log"></pre></div>

<script type="text/javascript" charset="utf-8">
    var socket = io.connect();
    var log = document.getElementById("log");
    var status = document.getElementById("status");

    socket.on('connect', function() {
        var status = document.getElementById("status");
        status.innerHTML = "Connected!"
    });
    socket.on('disconnect', function(reason) {
        var status = document.getElementById("status");
        status.innerHTML = "Disconnected: " + reason;
    });
    socket.on('update', function(msg) {
        on_update(msg.data);
    });

    function on_update(data){
        const jsonString = JSON.stringify(data, null, 2);
        log.innerHTML = jsonString;
    }
</script>
</body>
</html>
"""

class OverlayServer(Thread):
    def __init__(self, base_dir=None, host="", port=8991):
        super().__init__()
        self.base_dir = base_dir
        self.host = host
        self.port = port
        self._loop = asyncio.new_event_loop()
        self.sio = socketio.AsyncServer(async_mode='aiohttp')
        self.app = web.Application()
        self.runner = web.AppRunner(self.app)
        self.stop_event = asyncio.Event()
        self.sio.attach(self.app)
        self.app.router.add_static("/", self.base_dir)
        self.app.router.add_get('/', self.index)
        self.clients = []
        self.event_queue = queue.Queue()
        self.register_events()

    def get_url(self):
        host = "localhost"
        if self.host != "":
            host = self.host
        return f"http://{host}:{self.port}"
    
    async def index(self, request):
        index_path = os.path.join(self.base_dir, "index.html")
        if not os.path.exists(index_path):
            with open(index_path, "w") as f:
                f.write(INDEX_HTML)

        with open(index_path) as f:
            return web.Response(text=f.read(), content_type='text/html')
        
    def register_events(self):
        @self.sio.event
        async def connect(sid, environ):
            self.clients.append(sid)

        @self.sio.event
        def disconnect(sid, reason):
            self.clients.remove(sid)

    async def disconnect_all_clients(self):
        for client in self.clients:
            await self.sio.disconnect(client)
        self.clients = []

    def send_event(self, event, data):
        #self.event_queue.put((event,{"data": data}))
        self.event_queue.put((event,data))

    async def start_server(self):
        await self.runner.setup()
        site = web.TCPSite(self.runner, host=self.host, port=self.port)
        await site.start()

    async def wait_for_shutdown(self):
        await self.stop_event.wait()
        await asyncio.sleep(2)
        tasks = asyncio.all_tasks()
        for task in tasks:
            try:
                task.cancel()
                await task
            except asyncio.CancelledError:
                pass
            except asyncio.exceptions.CancelledError:
                pass
        await self.runner.cleanup()

    async def broadcast(self, msg):
        await self.sio.emit("broadcast", msg)

    async def send_events(self):
        while not self.stop_event.is_set():
            await asyncio.sleep(0)
            if self.event_queue.empty():
                continue
            event = self.event_queue.get_nowait()
            await self.sio.emit(event[0], event[1])

    def run(self):
        asyncio.set_event_loop(self._loop)
        tasks = asyncio.gather(self.start_server(), self.send_events(), self.wait_for_shutdown())
        try:
            self._loop.run_until_complete(tasks)
        except asyncio.exceptions.CancelledError:
            pass
        except OSError:
            pass

    def shutdown(self):
        self._loop.call_soon_threadsafe(self.stop_event.set)
