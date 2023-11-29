
## Cost functions

y true value
z=w*x + b

neuron's prediction
$\sigma(z)=a $ 


quadratic cost function
$C = \frac{1}{2n}\sum_x ||y(x)  - a^L(x)||^2  $
$a^L$ activation output of the L layer (L=last layer)

Cost function is a function of 4 main components :
$C(W,B,S^r , E^r)$
$S^r$ : input of a single training sample
$E^r$ : desired output of that training sample 

## Gradient descent
minimize our loss/cost with w

Learning rate = step size

Adaptive gradient descent
Adam : a method for stochastic optimization

When dealing with N-dimensional vectors (tensors) the notation changes from derivative to gradient, this means we calculate :
∇C(W1,W2,...,Wn) (upside down triangle is the way to notate gradient)

For classification problems, we use the **Cross entropy** loss function. Assumption is that the model predicts a probability distribution p(y=i) for each class i=1,2,...,C

For a binary classification :
$-(ylog(p) + (1-y)log(1-p))$

For M number of classes >2
$-\sum_{c=1}^My_{0,c} log(P_{0,c}) $

## backpropagation

For the last layer :

$Z^L = w^La^{L-1} + b^L $
$ x = a^{L-1} $
$a^L = \sigma(Z^L) $
$C_0 (...) = (a^L - y)^2 $

reminder
$C = \frac{1}{2n}\sum_x ||y(x)  - a^L(x)||^2  $

We want to understand how sensitive is the cost function to change in w:
$\frac{\delta C_O}{\delta w^L} $ Partial derivative of the cost function with respect to weights

There is a chain rule :

$\frac{\delta C_O}{\delta w^L} = \frac{\delta z^L}{\delta w^L} \frac{\delta a^L}{\delta z^L} \frac{\delta C_O}{\delta a^L} $ 

And we can do the same for the bias :

$\frac{\delta C_O}{\delta b^L} = \frac{\delta z^L}{\delta b^L} \frac{\delta a^L}{\delta z^L} \frac{\delta C_O}{\delta a^L} $ 

Hadamard product

$\begin{bmatrix}
1 \\ 2 \end{bmatrix} ⨀ \begin{bmatrix} 3 \\ 4 \end{bmatrix}  = \begin{bmatrix} 1 & * & 3 \\ 2 & *& 4 \end{bmatrix} = \begin{bmatrix} 3 \\ 8 \end{bmatrix}$ 

## Step 3 : compute our error vector

$\delta^L = ∇_a C ⨀ \sigma^l (Z^L)   $

$∇_a C = (a^L -y) $ expressing the rate of change of C with respect to the output activations

y is the true value

## step 4 : backpropagate the error

for each layer L-1, L-2 ... we compute 

$\delta^l = (W^{l+1})^T \delta^{l+1} ⨀ \sigma^l (Z^l)   $
$ (W^{l+1})^T$ is the transpose of the weight matrix of $l+1$ layer

The gradient of the cost function is given by :

for each layer L-1, L-2 ... we compute 
$\frac{\delta C}{\delta w^l_{jk}}  = a^{l-1}_k \delta ^l_j $ 
$\frac{\delta C}{\delta b^l_{j}}  = \delta ^l_j $ 

http://neuralnetworksanddeeplearning.com/chap2.html
https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
