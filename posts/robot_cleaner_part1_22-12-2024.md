
## Designing a robot vacuum cleaner (part 1)

This is my 'off the cuff' journey of designing and building a robot vacuum.
I love robotics and find cleaning to be a bit of a chore, mostly thanks to my 2 furry little
friends (dogs), why not convince myself it will be a good use of my time instead of just buying a consumer unit? How hard could it be... I will be using the terms vacuum and hoover interchangably because I'm based in the UK.

### Ideas and thoughts

The chassis/base is something I can build, I have access to 3D printers, motors and various SBCs etc. The design is likely to be nothing ground breaking, a dual motor drive system for tank style propulsion with a lidar sticking out of the top of a circular design. The rotating whiskers seem to be a staple of every consumer unit, they make sense so they will also making an appearance.

I have a lidar unit I bought on an impulse sat gathering dust. That should be ideal for room mapping and object detection. I also have an idea for projecting a laser onto the floor and detecting dirt/dust with a camera but that can wait until later.

Suction is something I might lift out of a existing handheld hoover although I would like to at least try my hand at it. Quadcopter motors can achieve incredible RPMs while being absolutely tiny. The motor controller and battery systems are also relatively cheap. That being said I have no idea how to design a vacuum.. chamber? How do you achieve negative pressure delta without exposing the motors/rotors to dust?

Some units employ an ultrasonic transducer to agitate the dust in at attempt to dislodge it from the floor. I couldn't find a module that would be suitable but maybe I'm just using the wrong search terms. Maybe shelve that for v2 (or v3).

A base unit for charging and self-emptying would be very cool. I assume the base 'sucks' the onboard dirt chamber into itself.

I will write the software from scratch using C++. Python is probably better suited for something like this due to the plethora of existing robotics control libraries and frameworks but I would atleast like to try my hand at it first. I can always have a look for some 'inspiration' if I get stuck later.

Driving stepper motors requires toggling pins pretty quickly for smooth motor control, this is probably best delegated to a lower power controller, something like an Arduino or PICO board. I can send commands over a serial connection and the main controller can focus on the hard bits (mapping, route planning).

Positional feedback of the steppers can be achieved with some [AS5600 Magnetic Encoders](https://www.amazon.co.uk/AITRIP-Magnetic-Induction-Measurement-Precision/dp/B09GLPV6WB/ref=pd_day0_d_sccl_2_5/259-9996061-4732954?pd_rd_w=KNFdK&content-id=amzn1.sym.c792d7a5-9034-43f8-85bb-20091edc6b5f&pf_rd_p=c792d7a5-9034-43f8-85bb-20091edc6b5f&pf_rd_r=Y8M5MQQKR5MDVKAQQ4P1&pd_rd_wg=Aokpo&pd_rd_r=121f2792-f9d6-4d45-b93c-ae74027f4f9d&pd_rd_i=B09GLPV6WB&psc=1). I need to workout how to fix the magnet to the shaft on the rear of the motor. I can 3d print an enclosure to hold the board.

Some of the parts I already have on hand are:

    - Nema 14 stepper motors
    - TMC2209 (or similiar) driver boards
    - Raspberry pi 5
    - Arduino Mega 2560 or Pico.
    - AS5600 Magnetic Encoders
    - USB lidar unit (the exact model escapes me right now).

I think I will spend some time laying out these parts in Fusion 360 until it feels right and print out a few dummy designs while thinking about how to design the vacuum system.
