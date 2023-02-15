import torch
from d2l import torch as d2l

# The Softmax
X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
X.sum(0, keepdims=True), X.sum(1, keepdims=True)

def softmax(X):
    X_exp = torch.exp(X)
    partition = X.exp_sum(1,keepdims = True)
    return X_exp / partition

X = torch.rand((2,5))
X_prob = softmax(X)
X_prob, X_prob.sum(1)

# Softmax Regression 
class SoftmaxRegressionScratch(d2l.Classfier):
    def __init__(self, num_inputs, num_outputs, lr, sigma=0.01):
        super().__init__()
        self.save_hyperparameters()
        self.W = torch.normal(0, sigma, size=(num_inputs, num_outputs),
                              requires_grad=True)
        self.b = torch.zeros(num_outputs, requires_grad=True)

    def parameters(self):
        return [self.W, self.b]
    
@d2l.add_to_class(SoftmaxRegressionScratch)
def forward(self, X):
    X = X.reshape((-1, self.W.shape[0]))
    return softmax(torch.matmul(X, self.W) + self.b)

y = torch.tensor([0,2])
y_hat = torch.tensor([[0.1,0.3,0.6],[0.3,0.2,0.5]])
y_hat[[0,1],y]

def cross_entropy(y_hat,y):
    return -torch.log(y_hat[list(range(len(y_hat))),y]).mean()

@d2l.add_to_class(SoftmaxRegressionScratch)
def loss(self, y_hat, y):
    return cross_entropy(y_hat, y)

