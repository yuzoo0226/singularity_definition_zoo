import os
import cv2
import argparse
from PIL import Image


class MediaConverter:
    """
    クラス: MediaConverter
    JPG画像をGIFアニメーションまたはMP4動画に変換するクラス
    """
    def __init__(self, input_dir: str, output_file: str, duration: int = 500):
        """
        初期化メソッド
        :param input_dir: JPG画像が含まれるフォルダのパス
        :param output_file: 出力するファイルのパス（GIFまたはMP4）
        :param duration: GIFまたはMP4のフレーム間隔（ミリ秒）
        """
        self.input_dir = input_dir
        self.output_file = output_file
        self.duration = duration
        self.frame_rate = 1000 / duration  # フレームレート (fps)

    def _load_images(self):
        """
        JPG画像をロードしてリストで返す
        :return: ロードしたImageオブジェクトのリスト
        """
        jpg_files = [f for f in os.listdir(self.input_dir) if f.lower().endswith('.jpg')]
        if not jpg_files:
            raise FileNotFoundError("指定したフォルダにJPG画像が見つかりません。")

        jpg_files.sort()  # ファイル名でソート
        return [Image.open(os.path.join(self.input_dir, file)) for file in jpg_files]

    def convert_to_gif(self):
        """
        JPG画像をGIFアニメーションに変換
        """
        images = self._load_images()
        images[0].save(
            self.output_file,
            save_all=True,
            append_images=images[1:],
            duration=self.duration,
            loop=0
        )
        print(f"GIFファイルが正常に作成されました: {self.output_file}")

    def convert_to_mp4(self):
        """
        JPG画像をMP4動画に変換
        """
        jpg_files = [f for f in os.listdir(self.input_dir) if f.lower().endswith('.jpg')]
        if not jpg_files:
            raise FileNotFoundError("指定したフォルダにJPG画像が見つかりません。")

        jpg_files.sort()  # ファイル名でソート

        # 1つ目の画像を読み込み、ビデオのサイズを設定
        first_image_path = os.path.join(self.input_dir, jpg_files[0])
        first_image = cv2.imread(first_image_path)
        height, width, _ = first_image.shape
        video_writer = cv2.VideoWriter(
            self.output_file,
            cv2.VideoWriter_fourcc(*'mp4v'),  # コーデック
            self.frame_rate,
            (width, height)
        )

        # 各画像をビデオに追加
        for file in jpg_files:
            img_path = os.path.join(self.input_dir, file)
            image = cv2.imread(img_path)
            video_writer.write(image)

        video_writer.release()
        print(f"MP4ファイルが正常に作成されました: {self.output_file}")


def main():
    """
    メイン関数: 引数の処理とクラスの呼び出し
    """
    parser = argparse.ArgumentParser(description="JPG画像をGIFまたはMP4に変換するツール")
    parser.add_argument(
        "--input_dir",
        type=str,
        # default="/home/tamhome/usr/yuga_ws/hsrtx_ws/pkls/tidyup_trial_57/demo-57/002/image_hand",
        # default="/home/tamhome/usr/yuga_ws/hsrtx_ws/pkls/tidyup_trial_79/demo-79/032/image_hand",
        # default="/home/tamhome/usr/yuga_ws/hsrtx_ws/pkls/tidyup_trial_31/demo-31/002/image_hand",
        # default="/home/tamhome/usr/yuga_ws/hsrtx_ws/pkls/tidyup_trial_112/demo-112/002/image_hand",
        default="/home/tamhome/usr/gs_ws/datasets/lerf_ovs/waldo_kitchen/images",
        help="JPG画像が格納されたフォルダのパス (デフォルト: ./images)"
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="/home/tamhome/usr/gs_ws/datasets/lerf_ovs/waldo_kitchen/kitchen.mp4",
        help="出力するGIFファイルのパス (デフォルト: output.gif)"
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=500,
        help="GIFまたはMP4のフレーム間隔（ミリ秒） (デフォルト: 500)"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["gif", "mp4"],
        default="mp4",
        help="出力フォーマットを指定（gif または mp4） (デフォルト: gif)"
    )
    args = parser.parse_args()

    # MediaConverterクラスのインスタンスを作成
    converter = MediaConverter(
        input_dir=args.input_dir,
        output_file=args.output_file,
        duration=args.duration
    )

    # フォーマットに応じて変換を実行
    if args.format == "gif":
        converter.convert_to_gif()
    elif args.format == "mp4":
        converter.convert_to_mp4()


if __name__ == "__main__":
    main()
