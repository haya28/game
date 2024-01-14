import random as r
import pygame as pg

class snake:

  def __init__(self):
    self.size = 1
    self.position = []
    self.score = 0
    self.color = (0.0.0)
  def main():

    # 初期化処理
    pg.init()
    pg.display.set_caption('蛇ゲーム')
    disp_w, disp_h = 800, 600
    screen = pg.display.set_mode((disp_w,disp_h))
    clock  = pg.time.Clock()
    exit_flag = False
    exit_code = '000'