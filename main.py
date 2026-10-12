
x = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 0, 0, 1]  # AND kapısı

w1, w2, b = 0.1, 0.1, -0.1
lr = 0.1
batch_size = epoch_size = len(x)
epoch = 0
loss = 1

while loss != 0:
    loss = 0
    for i in range(len(x)):
        z = w1*x[i][0] + w2*x[i][1] + b
        out = 1 if z >= 0 else 0
        error = y[i] - out
        loss += abs(error)
        w1 += lr * error * x[i][0]
        w2 += lr * error * x[i][1]
        b += lr * error
    epoch += 1
    print("Epoch:", epoch, "Loss:", loss)

print("Sonuc: Hata sifirlandi.")
print("Agirliklar:", w1, w2, "Bias:", b)

