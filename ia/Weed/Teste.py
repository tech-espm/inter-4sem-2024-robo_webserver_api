import cv2
import os
import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers

def main():

    # Avaliar o modelo
    test_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

    test_generator = test_datagen.flow_from_directory(
        'C:/Users/felipe.botelho/Desktop/Weed/Weed_Crop_Detection/test',
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical',
        shuffle=False
    )

    # Avaliação do modelo
    loss, accuracy = model.evaluate(test_generator)
    print(f'Test Accuracy: {accuracy:.2f}')
    print(f'Test Loss: {loss:.2f}')

if __name__ == "__main__":
    main()

# Função para carregar dados de weed_bounding_boxes
def load_bounding_box_data(image_folder, annotation_folder):
    images = []
    labels = []

    for filename in os.listdir(image_folder):
        if filename.endswith(('.jpg', '.png')):  # Ler todas as imagens
            img_path = os.path.join(image_folder, filename)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (150, 150))  # Ajuste para o tamanho desejado
            images.append(img)

            # Ler o arquivo de anotação correspondente
            annotation_path = os.path.join(annotation_folder, filename.replace('.jpg', '.txt'))
            if os.path.exists(annotation_path):
                with open(annotation_path, 'r') as f:
                    for line in f.readlines():  # Ler todas as linhas
                        parts = line.strip().split()
                        category_id = int(parts[0])
                        if category_id == 1:  # Apenas ervas daninhas
                            labels.append(1)
                            break
                    else:
                        labels.append(0)  # Se não houver rótulo, adicionar 0

    return images, labels

# Função para carregar dados de weed_crop_detection a partir do JSON
def load_data_from_json(json_file, image_folder):
    with open(json_file) as f:
        data = json.load(f)

    images = []
    labels = []

    for item in data['images']:
        img_name = item['file_name']
        img_path = os.path.join(image_folder, img_name)
        img = cv2.imread(img_path)

        if img is not None:
            img = cv2.resize(img, (150, 150))
            images.append(img)

            # Verifique se a imagem possui anotações para ervas daninhas
            for annotation in data['annotations']:
                if annotation['image_id'] == item['id'] and annotation['category_id'] == 1:  # Apenas ervas daninhas
                    labels.append(1)  # Rótulo para ervas daninhas
                    break
            else:
                labels.append(0)  # Rótulo para imagens que não são ervas daninhas

    return images, labels

# Carregar os dados de weed_bounding_boxes
image_folder_bb = 'C:/Users/felipe.botelho/Desktop/Weed/weed_bounding_boxes/agri_data/data'  # Caminho onde estão as imagens
annotation_folder_bb = image_folder_bb  # Como estão no mesmo lugar
images_bb, labels_bb = load_bounding_box_data(image_folder_bb, annotation_folder_bb)

# Carregar os dados de weed_crop_detection
json_file = 'C:/Users/felipe.botelho/Desktop/Weed/Weed_Crop_Detection/train/_annotations.coco.json'
image_folder_cd = 'C:/Users/felipe.botelho/Desktop/Weed/Weed_Crop_Detection/train/'  # Onde estão as imagens
images_cd, labels_cd = load_data_from_json(json_file, image_folder_cd)

# Combinar as imagens e rótulos
combined_images = images_bb + images_cd
combined_labels = labels_bb + labels_cd

# Normalizar as imagens
combined_images = np.array(combined_images) / 255.0
combined_labels = np.array(combined_labels)

# Criar e compilar o modelo
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Usar 1 saída para binário
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
model.fit(combined_images, combined_labels, epochs=10, batch_size=32, validation_split=0.2)