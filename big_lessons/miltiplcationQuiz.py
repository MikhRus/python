import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        # allowRegexes - correct answers
        # blocklistRegexes - incorrect answers
        pyip.inputInt(prompt, allowRegexes=['^%s$' % (num1 * num2)], \
            blockRegexes=[('.*', 'Incorrect!')], \
                timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Your time is gone!')
    except pyip.RetryLimitException:
        print('Your limit is gone!')
    else:
        # If in Try correct value
        print('Good Job!')
        correctAnswers += 1
    time.sleep(1)
print('Your score: %s vs %s :Total queries' % (correctAnswers, numberOfQuestions))