from invoke import task


@task(optional=['tiedosto'])
def huffmanpakkaa(ctx, tiedosto=None):
    if tiedosto:
        ctx.run(f'python app/huffman.py -c {tiedosto}')
    else:
        ctx.run('python app/huffman.py')

@task(optional=['tiedosto'])
def huffmanpura(ctx, tiedosto=None):
    if tiedosto:
        ctx.run(f'python app/huffman.py -d {tiedosto}')
    else:
        ctx.run('python app/huffman.py')

@task
def huffmanohje(ctx):
    ctx.run('python app/huffman.py -h')

@task(optional=['tiedosto'])
def lzpakkaa(ctx, tiedosto=None):
    if tiedosto:
        ctx.run(f'python app/lz78.py -c {tiedosto}')
    else:
        ctx.run('python app/lz78.py')

@task(optional=['tiedosto'])
def lzpura(ctx, tiedosto=None):
    if tiedosto:
        ctx.run(f'python app/lz78.py -d {tiedosto}')
    else:
        ctx.run('python app/lz78.py')

@task(optional=['algoritmi'])
def suorituskyky(ctx, algoritmi=['huffman, lz78']):
    # if 'huffman' in algoritmi:
    ctx.run('python app/huffman_suorituskyky.py')

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