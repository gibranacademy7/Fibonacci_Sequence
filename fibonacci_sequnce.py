def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b    # التفكيك المتعدد (multiple assignment
    return sequence
n = 10
print(fibonacci_sequence(n));
#------------------------------------------

def fibonacci_sequence(n):
    sequence = [];
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a);
        a, b = b, a + b
    return sequence

#---------------------------------------------------------------------------------------
def quotient_of_consecutive_numbers(sequence):
    quotients = []
    for i in range(1, len(sequence)):
        if sequence[i-1] != 0:  # لتجنب القسمة على صفر
            quotients.append(sequence[i] / sequence[i-1]);
        else:
            quotients.append(None);  # أو يمكنك استخدام قيمة مختلفة مثل 0 أو رسالة تحذيرية
    return quotients

n = 10
fib_sequence = fibonacci_sequence(n);
print("Fibonacci Sequence:", fib_sequence);
print("Quotients of Consecutive Numbers:", quotient_of_consecutive_numbers(fib_sequence));
# الجزء من الكود يستدعي الدالة quotient_of_consecutive_numbers التي قمنا بتعريفها سابقًا.
# تقوم هذه الدالة بحساب نواتج قسمة كل رقمين متتاليين في القائمة fib_sequence، وهي القائمة التي تحتوي على تسلسل فيبوناتشي الناتج من الدالة fibonacci_sequence.
# الدالة تُعيد قائمة جديدة تحتوي على هذه النواتج.
