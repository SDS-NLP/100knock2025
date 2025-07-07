from knock72 import model, X_train, y_train
import torch
import torch.optim as optim
import torch.nn as nn

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

epochs = 20
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    
    # 順伝播
    outputs = model(X_train).squeeze()
    
    # 損失計算
    loss = criterion(outputs, y_train.squeeze())
    
    # 誤差逆伝播 & パラメータ更新
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch+1}: Loss = {loss.item():.4f}")
    

torch.save(model.state_dict(), "model.pth")
