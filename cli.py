import click
import shogicam
import shogicam.util
import shogicam.data

@click.group(help='shogi camera')
@click.pass_context
def main(ctx):
    pass

@main.command(help='Predict shogi board contents')
@click.pass_context
def predict(ctx):
    print("predict")

@main.command(help='Detect corner coordinates')
@click.argument('img_path', type=click.Path(exists=True))
@click.option('--out-img-path', '-o', type=click.Path(), default=None)
def corners(img_path, out_img_path):
    raw_img = shogicam.util.load_img(img_path)
    rect, score = shogicam.corners(raw_img)
    if out_img_path:
        drawed = shogicam.util.draw_rect(raw_img, rect)
        shogicam.util.save(drawed, out_img_path)
    rect = rect.tolist()
    decoded = {
        "coordinates": {
            "left-top": rect[0],
            "right-top": rect[1],
            "right-bottom": rect[2],
            "left-bottom": rect[3]
        },
        "score": score
    }
    print(decoded)

@main.command(help='Predict cell contents')
@click.pass_context
def predict_cell(ctx):
    print("predict-cell")

@main.command(help='Generate koma train data')
@click.argument('img_dir', type=click.Path(exists=True), default='images/koma')
@click.argument('outdata_dir', type=click.Path(exists=True), default='data/koma')
def gen_koma_traindata(img_dir, outdata_dir):
    result = shogicam.data.gen_koma_traindata(img_dir, outdata_dir)
    print(result)

if __name__ == '__main__':
    main()
