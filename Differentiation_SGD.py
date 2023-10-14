### Function minimization with automatic differentiation and SGD ###
import tensorflow as tf
import matplotlib.pyplot as plt



# Initialize a random value for our initial x
x = tf.Variable([tf.random.normal([1])])
print("Initializing x={}".format(x.numpy()))

learning_rate = 1e-2 # learning rate for SGD
history = []
# Define the target value
x_f = 4

# We will run SGD for a number of iterations. At each iteration, we compute the loss, 
#   compute the derivative of the loss with respect to x, and perform the SGD update.
for i in range(300):
    with tf.GradientTape() as tape:
        '''TODO: define the loss as described above'''
        loss = (x - x_f) ** 2

    # loss minimization using gradient tape
    grad = tape.gradient(loss, x) # compute the derivative of the loss with respect to x
    new_x = x - learning_rate*grad # sgd update
    x.assign(new_x) # update the value of x
    history.append(x.numpy()[0])

    plt.plot(history)
    plt.plot([0, 500],[x_f,x_f])
    plt.title(f'''SGD || loss = (x - 4)^2 || loss = {str(loss.numpy())} 
|| dy_dx = {grad.numpy()} || x = {x.numpy()} - lr * {grad.numpy()}''')
    plt.legend(('Predicted', 'True'))
    plt.xlabel('Iteration')
    plt.ylabel('x value')
    
    plt.savefig(f"D:\Project\pics\{i}")
# Plot the evolution of x as we optimize towards x_f!
