import torch
import torchvision.transforms as T
import numpy as np
import cv2
from PIL import Image


model = torch.hub.load('pytorch/vision:v0.10.0', 'deeplabv3_resnet101', pretrained=True)
model.eval()


transform = T.Compose([
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225])
])

input_image = Image.open("foreground.jpg").convert("RGB")
background_image = Image.open("background.jpg").convert("RGB").resize(input_image.size)


input_tensor = transform(input_image).unsqueeze(0)


with torch.no_grad():
    output = model(input_tensor)['out'][0]
output_predictions = output.argmax(0).byte().cpu().numpy()


person_class = 15
mask = output_predictions == person_class


input_np = np.array(input_image)
background_np = np.array(background_image)


background_np = cv2.resize(background_np, (input_np.shape[1], input_np.shape[0]))


output_image = np.where(mask[..., None], input_np, background_np)

cv2.imwrite("output.jpg", cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))
cv2.imshow("Result", cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()
