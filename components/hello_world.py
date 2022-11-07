import suanpan
from suanpan.app import app
from suanpan.app.arguments import String, Json, Csv
from suanpan.log import logger
# from suanpan.utils import image


@app.input(Csv(key="inputData1"))
@app.param(String(key="param_prefix", alias="prefix"))
@app.output(String(key="outputData1", alias="result"))
def hello_world(context):
    args = context.args
    logger.info(f'args:{args.prefix}')
    # image.read('aaa.png')
    return f'Welcome {args.prefix}!'


if __name__ == "__main__":
    suanpan.run(app)
