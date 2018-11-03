from flask import Response, escape
from app_mysql import app
from subprocess import Popen, PIPE, STDOUT

SENTINEL = '------------SPLIT----------HERE---------'
VALID_ACTIONS = ('what', 'ever')

def logview(logdata):
    """Render the template used for viewing logs."""
    # Probably a lot of other parameters here; this is simplified
    return render_template('wip.html', logdata=logdata)

def stream(first, generator, last):
    """Preprocess output prior to streaming."""
    yield first
    for line in generator:
        yield escape(line.decode('utf-8'))  # Don't let subproc break our HTML
    yield last

@app.route('/subprocess/<action>', methods=['POST'])
def perform_action(action):
    """Call subprocess and stream output directly to clients."""
    if action not in VALID_ACTIONS:
        abort(400)
    first, _, last = logview(SENTINEL).partition(SENTINEL)
    path = 'code2run.py'
    proc = Popen((path,), stdout=PIPE, stderr=STDOUT)
    generator = stream(first, iter(proc.stdout.readline, b''), last)
    return Response(generator, mimetype='text/html')

@app.route('/subprocess/<action>', methods=['GET'])
def show_log(action):
    """Show one full log."""
    if action not in VALID_ACTIONS:
        abort(400)
    path = '.'
    with open(path, encoding='utf-8') as data:
        return logview(logdata=data.read())
