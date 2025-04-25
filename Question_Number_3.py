import turtle

def draw_branches(t, length, depth, thickness, left_angle, right_angle, factor):
    if depth == 0:
        return

    t.color("green")
    t.width(thickness)
    t.forward(length)

    # Right branch
    t.right(right_angle)
    draw_branches(t, length * factor, depth - 1, thickness * 0.7, left_angle, right_angle, factor)

    # Left branch
    t.left(right_angle + left_angle)
    draw_branches(t, length * factor, depth - 1, thickness * 0.7, left_angle, right_angle, factor)

    # Restore state
    t.right(left_angle)
    t.backward(length)

# --- Main Program ---
left_angle = float(input("Enter left branch angle: "))
right_angle = float(input("Enter right branch angle: "))
start_length = float(input("Enter starting branch length: "))
depth = int(input("Enter recursion depth: "))
reduction_factor = float(input("Enter length reduction factor, eg 0.7: "))

t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
t.left(90)
t.up()
t.goto(0, -250)
t.down()

# Draw trunk
trunk_thickness = 10
t.color("brown")
t.width(trunk_thickness)
t.forward(start_length)

# Start branches from the top of trunk (after turning)
t.right(right_angle)
draw_branches(t, start_length * reduction_factor, depth - 1, trunk_thickness * 0.7, left_angle, right_angle, reduction_factor)

t.left(right_angle + left_angle)
draw_branches(t, start_length * reduction_factor, depth - 1, trunk_thickness * 0.7, left_angle, right_angle, reduction_factor)

t.right(left_angle)  # Restore orientation

turtle.exitonclick()
