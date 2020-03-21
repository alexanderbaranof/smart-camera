# Smart-camera project
![example detect](example.jpg)

Данные репозиторий содержит код для запуска системы умная камера.




Для запуска системы с полной версией модели необходимо запустить 

```
python3 scripts/detection.py —path_weights ./model_data/tiny-yolo_weights_full.h5 —path_anchors ./model_data/tiny-yolo_anchors.csv —path_classes ./train_classes.txt —path_output ./results —path_video 0
```


Для запуска модели с версией Tensorflow Lite необходимо запустить след. код:
```
python3 tf_lite_run.py
```

Пример работы алгоритма на большой аудитории
![yet another example](https://sun9-41.userapi.com/c855036/v855036216/1d8c32/1O5PEQ3o8EM.jpg)