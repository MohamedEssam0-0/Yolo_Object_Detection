# Road Surface Deterioration Detection Using AIoT

This project focuses on detecting road surface deterioration using the integration of Artificial Intelligence of Things (AIoT). It utilizes advanced machine learning models and IoT devices to identify and classify road damages, specifically cracks and potholes, with high accuracy and real-time processing capabilities.

## Table of Contents

1. [Introduction](#introduction)
2. [Motivation](#motivation)
3. [Aim of the Thesis](#aim-of-the-thesis)
4. [Project Architecture](#project-architecture)
5. [Methodology](#methodology)
6. [Results](#results)
7. [Future Work](#future-work)

## Introduction

The degradation of road surfaces presents significant challenges to transportation infrastructure, impacting safety, efficiency, and maintenance costs. Traditional methods of road maintenance often rely on manual inspections, which are labor-intensive and inefficient. This project proposes an AIoT-based system to automate the detection and classification of road surface damages.

## Motivation

Roads are essential for economic and social development. However, their deterioration poses risks to safety and leads to increased maintenance costs. This project aims to develop a proactive, efficient, and cost-effective system for road surface monitoring using AI and IoT technologies, allowing for real-time detection and timely repairs.

## Aim of the Thesis

The primary goal is to develop an automated system that leverages AI and IoT for detecting road surface deterioration. The objectives include:

- Implementing a robust AI model using the YOLO V8 architecture.
- Integrating IoT devices like Raspberry Pi 4 and Coral AI Dev Board Mini for real-time data capture and processing.
- Developing dynamic frame rate adjustments based on vehicle speed to optimize resource use.
- Evaluating the system's effectiveness in real-world conditions.

## Project Architecture

The project architecture consists of two main components:

1. **Edge Processing Unit**: Utilizes devices like Raspberry Pi 4 and Coral AI Dev Board Mini for image capture and preliminary processing. These devices run the AI model to detect road damages.

2. **Central Monitoring System**: Collects data from edge devices for further analysis and refinement of the AI model.

## Methodology

The methodology involves the following steps:

- **Dataset Sourcing**: Utilized the "Japan Image Dataset" from Roboflow, applying augmentations to enhance model training.
- **Model Training**: Employed the YOLO V8 architecture, trained on a MacBook Pro M3 Pro for initial development.
- **Real-Time Processing**: Implemented dynamic frame rate adjustment based on vehicle speed to maintain detection accuracy.
- **Microcontroller Integration**: Integrated Raspberry Pi for image capture and Coral AI Dev Board Mini for real-time inference.

## Results

The system demonstrated high accuracy in detecting road damages, achieving a mean average precision (mAP) of 0.511. The model processed video frames in real-time, adjusting frame rates dynamically based on vehicle speed to optimize detection performance.

## Future Work

Future enhancements include the development of a mapping system for detected damages and the integration of a more sophisticated IoT framework for collaborative detection using multiple vehicles. This approach aims to improve the system's reliability and applicability in diverse environments.

For more details on the implementation, see the Python code documentation and additional resources included in the repository.
