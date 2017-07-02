Using Student Learning Based on Fluency for the Learning Rate in a Deep Convolutional Neural Network
==

The full paper may be read at [ResearchGate](https://goo.gl/phlQNY)

## Abstract
This is a proposal for mathematically determining the learning rate to be used in a deep supervised convolutional neural network (CNN), based on student fluency. The CNN model shall be tasked to imitate how students play the game _Packet Attack_, a form of gamification of information security awareness training, and learn in the same rate as the students did. The student fluency shall be represented by a mathematical function constructed using natural cubic spline interpolation, and its derivative shall serve as the learning rate for the CNN model. If proven right, the results will imply a more human-like rate of learning by machines.


## Introduction
[Chen & Yi (2017)](https://arxiv.org/abs/1702.05663) successfully developed a deep convolutional neural network (CNN) that teaches a computer to play Super Smash Bros and Mario Tennis (both ran by using a Nintendo 64 emulator). However, like other neural networks\cite{Baird, Gupta, Jain, Lewandowsky, Negnevitsky, Riedmiller, Wilson}, the _learning rate_ in their model was a pre-programmed numerical constant. This research proposes to use a series of existing methods to mathematically determine what is the learning rate to be used in a neural network.

First, the aim is to measure the learning, based on fluency, of the players who will be subjected to the gamification of information security awareness traning. In this instance, the game to be played is about network packets, i.e. determining which is a _bad_ packet and a _good_ packet, named _Packet Attack_.

To accomplish the above goal, the data consisting the time of gameplay of players ($x$-axis) and the number of correct responses (_fluency_ in this context\cite{Chance}, $y$-axis) shall be the basis of constructing a mathematical function which will show the relationship between the data.

The mathematical function shall be constructed using _cubic spline interpolation_ since the graph of learning of individuals are usually not _smooth_, or in mathematical context, not differentiable at some points. The cubic spline interpolation produces a piecewise-polynomial function which gives a mathematical function at a specified interval like $[a,b]$ (see [Figure 1](figures/spline.png)). Hence, _smoothening_ the graph of learning (see [Figure 2](figures/spline_1.png)).
