# CodeSignal Problems

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [CodeSignal Problems](#codesignal-problems)
    - [How to use this repository](#how-to-use-this-repository)
    - [CodeSignal Arcade](#codesignal-arcade)
        - [Intro](#intro)
            - [Through the Fog](#through-the-fog)
                - [33: stringsRearrangement](#33-stringsrearrangement)
    - [Footnotes](#footnotes)

<!-- markdown-toc end -->


## How to use this repository

This repository is meant to be a resource for anyone wanting to learn
more about computer science, algorithms, or solving code
challenges. While it provides the solutions to real code challenges,
it is not designed as a cheat sheet; code challenges are a learning
resource, and if you use this repository to complete them without
learning anything the only person you will be cheating is yourself.

Each comment provides a link to the problem on the source
website. Ideally, you should complete the problem yourself, and then
compare it to the solution provided here. If you feel you are
completely stumped you should read my discussion of the problem, and
then see if you can complete it yourself with that help. My solution
is also provide both with and without commentary. You should not look
at these solutions unless you have completely given up on solving the
problem.

Finally, a small bit of self-promotion. If you feel my solution, or
any other solution found on this repository, is more understandable
than the current top voted solutions, please up-vote it. Let's try to
get the opaque, barely readable solutions knocked off the top of the
leaderboards on the code challenge web sites.

Lastly, pull requests are welcome with any corrections, superior
solutions, solutions to problems not already documented, or solutions
in other programming languages. All solutions should include a
commentary section in this file. If you cannot do a pull request for
any reason, you can submit any changes as an issue on GitHub, or email
them the me, Harry Henry Gebel, at harry@gebel.tech. Please be sure to
credit yourself in any solutions and commentary you submit,
submissions that do not give themselves proper credit will not be
merged.

## CodeSignal Arcade

### Intro

#### Through the Fog

##### 33: stringsRearrangement

[CodeSignal problem](https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9) |
[My solution](https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9/solutions?solutionId=cNGxjcQ9Mti5fmTNe) |
[commented](stringsRearrangement-commented.py) |
[uncommented](stringsRearrangement.py)

Test an array of equal-length words to see if they can be arranged in
any order such that each word in the sequence is exactly one character
different than the preceding word. Return true if at least one such
sequence exists.

This is an interesting problem, because as far as I can tell the
optimal solutions all have factorial<sup>[1](#factorial)</sup> time
complexity. Most solutions had quadratic<sup>[2](#quadratic)</sup>
space complexity (although one of the other solutions had factorial
space complexity as well!) The unusually high time complexity of the
solution is probably the reason that the constraints limit the number
of words in the array to 10, this holds the worst case maximum number
of permutations down to around 3.6
million.<sup>[3](#10-factorial)</sup> Most CodeSignal problems provide
input arrays with thousands of elements for the larger hidden tests,
but that is because most CodeSignal problems to not have an inherent
factorial time complexity. Still, even with the small input size, we
must be as efficient as possible to finish with the time limit (4
seconds for Python) with a full 10 element input array.

This question requires you to examine every permutation (every
possible arrangement) of the input array elements to see if one meets
the test conditions. An list of items has a number of permutations
equal to the factorial of the number of items in the list. Factorials
grow extremely quickly, the 10 word maximum in this problem's
constraints has 3.6 million permutations. This can be solved in a few
seconds. If the number of words was doubled to 20 there would be 2.4
quintillion permutation, meaning that if you could check 1 billion
permutations per second the function call would take 77 years to
return. Add just 5 more words would bring the total number of
permutations to 15 septillion, and at a billion permutations per
second the function would take almost 492 million years to
return. Obviously, the input of functions with factorial time
complexity must be kept as short as possible.

There are several options for this solution that can complete in the 4
second Python time limit. If you are using Python the `itertools`
module provides a function, `permutations`, which returns an iterator
that will provide each permutation of the input array in
sequence. Each permutation can then be checked to see if it satisfies
the criteria. The other possible solution is to write a recursive
function that checks each permutation by checking all possible
permutations of lists each of which is one shorter than the last.

The iterator solution completes all CodeSignal tests successfully,
although there may be untested pathological input sets that would
cause it to exceed the time limit. The recursive solution should be
somewhat faster because the iterator will check every permutation,
while the recursive solution will not check any permutations that have
already been proven false due to sharing a proven false set of first
several words. The input limit of 10 words, while guaranteeing that
the problem can be completed within CodeSignal's time limit, also
means that there is no danger of the recursive solution exceeding the
capacity of the stack, the largest worry when using a recursive
function in a language like Python that does not feature tail call
optimization.

I chose a recursive solution. Either solution will work. A warning to
those who choose to use `itertools.permutations`, do not do what the
following solution did:

```python
def stringsRearrangement(inputArray):
    import itertools
    l=list(itertools.permutations(inputArray))
    for i in range(len(l)):
        c2=0
        for j in range(len(l[0])-1):
            c1=0
            for k in range(len(l[0][0])):
                if(l[i][j][k])!=(l[i][j+1][k]):
                    c1+=1
            if c1==1:
                c2+=1
        if c2>=(len(l[0]))-1:
            return True
    return False
```

This is pretty opaque with the inscrutable variable names,
difficult-to-read formatting, and strange decision to import a module
inside of a function, but that is not it's problem. Line three is the
problem; it takes the iterator and makes a list with every
permutation! With a full 10 word array using the maximum 15 character
long words provide by the problem constraints this list will take
approximately 540 megabytes! While obviously CodeSignal provides
enough memory that this passed all the tests, it is really
unacceptable to use 540 megabytes of memory on a solution that would
normally use less than a kilobyte, without providing any increase in
speed or readability! You can loop over an iterator in exactly the
same way you loop over a list, and an iterator only takes up as much
memory as the last permutation, not as much memory as all 3.6 million
permutations as this solution uses. Not to mention the list probably
took around a half second to produce, that's a lot more time out of
your precious 4 seconds than you want to spend building a data
structure that doesn't even need to exist in the first place.

## Footnotes

<a name="factorial"><sup>1</sup></a> O(n!)<br>
<a name="quadratic"><sup>2</sup></a> O(n^2)<br>
<a name="10-factorial"><sup>3</sup></a> 10! = 3,628,800<br>
20! = 2,432,902,008,176,640,000<br>
25! = 15,511,210,043,330,985,984,000,000<br>

Calculations performed using Steel Bank Common Lisp with the following
factorial function:

```common-lisp
* (defun ! (n)
    (if (zerop n)
        1
        (* n (! (- n 1)))))
!
* (! 10)
3628800
* (! 20)
2432902008176640000
* (! 25)
15511210043330985984000000
```


<!--  LocalWords:  stringsRearrangement
 -->
