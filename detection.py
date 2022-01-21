import cv2
import imutils


class Detection:

    def __init__(self, args):
        self._hog = cv2.HOGDescriptor()
        self._hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self._args = args

    def detectByPathImage(self):
        image = cv2.imread(self._args['image'])
        output_path = self._args['output']
        image = imutils.resize(image, width=min(450, image.shape[1]))
        result_image = self.detect(image)
        if output_path is not None:
            cv2.imwrite(output_path, result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def detect(self, image):
        rects, weights = self._hog.detectMultiScale(image,
                                                    winStride=(4, 4),
                                                    padding=(32, 32),
                                                    scale=1.08)
        person = 0
        for x, y, w, h in rects:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 3)
            cv2.putText(image, f'person {person + 1}', (x, y),
                        cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 0), 1)
            person += 1
        cv2.imshow('output', image)
        print(f'Total person detected: {person}')
        return image
