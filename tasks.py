from invoke import task


@task
def huffmanpakkaa(ctx, tiedosto=None):
    if tiedosto:
        ctx.run(f'python app/huffman.py -c {tiedosto}')
    else:
        ctx.run(f'python app/huffman.py')

@task
def huffmanpura(ctx, tiedosto=None):
    if tiedosto:
        ctx.run(f'python app/huffman.py -d {tiedosto}')
    else:
        ctx.run(f'python app/huffman.py')

@task
def huffmanohje(ctx):
    ctx.run('python app/huffman.py -h')

@task
def lzpakkaa(ctx, tiedosto=None):
    if tiedosto:
        ctx.run(f'python app/lz78.py -c {tiedosto}')
    else:
        ctx.run(f'python app/lz78.py')

@task
def lzpura(ctx, tiedosto=None):
    if tiedosto:
        ctx.run(f'python app/lz78.py -d {tiedosto}')
    else:
        ctx.run(f'python app/lz78.py')

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