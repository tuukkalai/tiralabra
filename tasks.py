import os
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
    if 'huffman' in algoritmi:
        ctx.run('python app/huffman_suorituskyky.py')
    elif 'lz78' in algoritmi:
        ctx.run('python app/lz78_suorituskyky.py')
    else:
        ctx.run('python app/huffman_suorituskyky.py && python app/lz78_suorituskyky.py')

@task
def siivoa(ctx):
    siivottavat = [
        os.path.join(hakemisto, tiedosto)
        for hakemisto, hakemisto_nimi, tiedosto_nimi in os.walk(os.path.join(os.getcwd(), 'data'))
        for tiedosto in tiedosto_nimi
        if os.path.splitext(tiedosto)[1] in ['.huff', '.lz', '.purettu']
    ]
    for tiedosto in siivottavat:
        ctx.run(f'rm {tiedosto}')

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