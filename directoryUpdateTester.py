import os
import time
import detect

path_to_watch = "./images"
before = dict([(f, None) for f in os.listdir(path_to_watch)])
while 1:
  time.sleep(10)
  after = dict([(f, None) for f in os.listdir(path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added:
    print ("Added: ", ", ".join(added))
    detect.run(weights="best3.pt", source=path_to_watch, data="Volume_Detection_ExtraClass_Nov18/data.yaml", save_crop=True, conf_thres=0.4, iou_thres=0.45,save_conf=True)
  if removed:
    print ("Removed: ", ", ".join(removed))
  before = after
