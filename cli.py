import click
import shogicam
import shogicam.util
import shogicam.data
import shogicam.learn

@click.group(help='shogi camera')
def main():
    pass

@main.command(help='Predict shogi board contents')
@click.pass_context
def predict(ctx):
    print("predict")

@main.command(help='Fit model')
@click.option('--data-dir', '-d', type=click.Path(exists=True), default='data')
@click.option('--outmodel-path', '-o', type=click.Path(), default='models/purple.h5')
@click.option('--model', '-m', default='purple')
def learn(data_dir, outmodel_path, model):
    model = shogicam.learn.purple(data_dir, verbose=True)
    shogicam.learn.save_model(model, outmodel_path)

@main.group(help='Generate train data')
def gen_traindata():
    pass

@gen_traindata.command(help='Generate koma train data')
@click.option('--img-dir', '-i', type=click.Path(exists=True), default='images/koma')
@click.option('--outdata-dir', '-o', type=click.Path(exists=True), default='data/koma')
def koma(img_dir, outdata_dir):
    result = shogicam.data.gen_koma_traindata(img_dir, outdata_dir)
    print(result)

@gen_traindata.command(help='Generate empty cell train data')
@click.option('--img-dir', '-i', type=click.Path(exists=True), default='images/empty_cell')
@click.option('--outdata-path', '-o', type=click.Path(), default='data/empty_cell.npz')
def empty_cell(img_dir, outdata_path):
    result = shogicam.data.gen_empty_cell_traindata(img_dir, outdata_path)
    print(result)

@main.command(help='Predict cell contents')
@click.pass_context
def predict_cell(ctx):
    print("predict-cell")

@main.command(help='Detect corner coordinates')
@click.argument('img_path', type=click.Path(exists=True))
@click.option('--out-img-path', '-o', type=click.Path(), default=None)
def detect_corners(img_path, out_img_path):
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

if __name__ == '__main__':
    main()
