# Enhancing the Performance of Early Detection of Melanoma Skin Cancer

This repository contains the official implementation, source code, and experimental results for the paper focused on improving early melanoma skin cancer detection. The primary objective of this project is to address class imbalance in dermatological datasets using Generative Adversarial Networks (GANs) and evaluate the quality of the generated data using deep learning architectures.

---

## Project Overview

Medical image datasets for melanoma detection often suffer from severe class imbalance, which can bias machine learning models toward majority classes. This project explores the efficacy of various GAN architectures to synthesize high-quality, realistic skin lesion images to balance the dataset, ultimately aiming to improve the robustness and accuracy of early detection systems.

---

## Methodology

### 1. Data Balancing (GANs)
To handle the dataset imbalance, we implemented and compared three distinct Generative Adversarial Network architectures:
* **WGAN (Wasserstein GAN):** Utilizes the Wasserstein distance to improve training stability and prevent mode collapse.
* **RALSGAN (Relativistic Average Least Squares GAN):** Evaluates the probability that the real data is more realistic than the generated data, enhancing gradient stability.
* **CycleGAN:** Used for image-to-image translation tasks to adapt and augment existing lesion characteristics across domains.

### 2. Evaluation
* **VGG16:** A pre-trained VGG16 network was utilized to evaluate the quality, feature distribution, and classification performance of the balanced dataset against baseline models.

---

## Repository Structure

```text
├── data/               # Code or placeholders for datasets
├── models/             # Implementations of WGAN, RALSGAN, CycleGAN, and VGG16
├── notebooks/          # Jupyter notebooks for experimentation and visualization
├── results/            # Evaluation metrics, generated images, and performance plots
├── src/                # Core source code for training and preprocessing
├── requirements.txt    # List of required Python dependencies
└── README.md           # Project documentation
