import numpy as np
import matplotlib.pyplot as plt

def image_batch(batch, y_true, y_pred=None, labels=None, n_cols=10, figsize=(16,5)):
    plt.figure(figsize=figsize)
    
    y_pred = y_true if y_pred is None else y_pred
    labels = y_true if labels is None else labels
    n_rows = batch.shape[0] // n_cols + 1
    is_gray = (batch.ndim == 3)
    for img, true, pred, sub in zip(batch, y_true, y_pred, range(1, len(batch)+1)):
        plt.subplot(n_rows, n_cols, sub)
        plt.imshow(img.astype(np.uint8), cmap='gray' if is_gray else None)
        
        plt.title("{}".format(labels[sub-1]), color = 'green' if true == pred else 'red')
        plt.axis('off')
    plt.tight_layout()