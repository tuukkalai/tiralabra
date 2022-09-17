from invoke import task

@task
def start(ctx):
    ctx.run('python app/huffman.py')

@task
def test(ctx):
    ctx.run('pytest app')

@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest app')

@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage report')

@task(coverage)
def coverage_html(ctx):
    ctx.run('coverage html')

@task
def format(ctx):
    ctx.run('black app')