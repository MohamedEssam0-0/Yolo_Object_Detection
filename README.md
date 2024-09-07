# Road Surface Deterioration Detection Using AIoT

Welcome to the Road Surface Deterioration Detection project! This project employs Artificial Intelligence of Things (AIoT) technology to detect and classify road surface deterioration, such as cracks and potholes.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Project Architecture](#project-architecture)
4. [Methodology](#methodology)
5. [Results](#results)
6. [Future Work](#future-work)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

This project investigates the application of AIoT technology specifically focusing on cracks and potholes. Our approach utilizes the "Japan Image Dataset" from Roboflow, applying augmentations to enhance the model's ability to generalize from training data to real-world scenarios.

## Features

- **Real-Time Detection**: Utilizes YOLO V8 model to detect road damage.
- **Dynamic Frame Rate Adjustment**: Adjusts frame processing based on vehicle speed.
- **Microcontroller Integration**: Uses Raspberry Pi 4 and Coral AI Dev Board Mini for efficient processing.
- **Scalable**: Designed to work across various road types and conditions.

## Project Architecture

The architecture of the project is divided into two main components:

1. **Edge Processing Unit**: Includes IoT devices like the Raspberry Pi 4 and Coral AI Dev Board Mini for image capture and initial processing.
2. **Central Monitoring System**: Collects data from edge devices for further analysis and system validation.

## Methodology

- **Dataset**: Utilizes the "Japan Image Dataset" for training.
- **Model**: YOLO V8 architecture for object detection.
- **Real-Time Processing**: Dynamic adjustment of frame rates based on vehicle speed.
- **IoT Integration**: Uses Raspberry Pi for image capture and Coral AI for inference.

## Results

The model achieved a mean average precision (mAP) of 0.511 with high precision and recall rates, demonstrating robust detection capabilities.

## Future Work

- Implement a mapping system for detected damages.
- Enhance IoT framework for collaborative detection using multiple vehicles.

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
