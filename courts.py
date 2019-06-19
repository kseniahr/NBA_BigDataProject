from matplotlib.patches import Circle, Rectangle, Arc
import matplotlib.pyplot as plt

def draw_court(ax=None, color='black', lw=2, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    backboard1 = Rectangle((50, 225), -1, 50, linewidth=lw, color=color)
    backboard2 = Rectangle((895, 225), 1, 50, linewidth=lw, color=color)

    hoop1 = Circle((60, 250), radius=6, linewidth=lw, color=color, fill=False)
    hoop2 = Circle((885, 250), radius=6, linewidth=lw, color=color, fill=False)

    restricted1 = Arc((50, 250), 80, 80, angle=270, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    restricted2 = Arc((895, 250), 80, 80, angle=270, theta1=180, theta2=0, linewidth=lw,
                     color=color)

    freethrow1_outer = Arc((195, 250), 100, 120, angle=270, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    freethrow2_outer = Arc((755, 250), 100, 120, angle=270, theta1=180, theta2=0, linewidth=lw,
                     color=color)

    freethrow1_inner = Arc((195, 250), 100, 120, angle=270, theta1=180, theta2=0, linewidth=lw,
                     color=color, linestyle='dashed')

    freethrow2_inner = Arc((755, 250), 100, 120, angle=270, theta1=0, theta2=180, linewidth=lw,
                     color=color, linestyle='dashed')

    threepoint1 = Arc((90, 250), 450, 400, angle=270, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    threepoint2 = Arc((850, 250), 450, 400, angle=270, theta1=180, theta2=0, linewidth=lw,
                     color=color)

    innerbox1 = Rectangle((20, 200), 175, 100, linewidth=lw, color=color,
                          fill=False)

    innerbox2 = Rectangle((920, 200), -175, 100, linewidth=lw, color=color,
                          fill=False)

    outbox1 = Rectangle((20, 190), 175, 120, linewidth=lw, color=color,
                          fill=False)

    outbox2 = Rectangle((930, 190), -175, 120, linewidth=lw, color=color,
                          fill=False)

    half_court_line = Rectangle((470, 0), 1, 500, linewidth=lw, color=color,
                          fill=False)

    half_court_circle  = Circle((470, 250), radius=60, linewidth=lw, color=color, fill=False)

    # List of the court elements to be plotted onto the axes
    court_elements = [backboard1, backboard2, hoop1, hoop2, restricted1,
                      restricted2, threepoint1, threepoint2, innerbox1,
                      innerbox2, freethrow1_outer, freethrow2_outer,
                      outbox1, outbox2, freethrow1_inner, freethrow2_inner,
                      half_court_line, half_court_circle]

    if outer_lines:
    # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((20, 0), 910, 500, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)

      # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    ax.set_aspect('auto')
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.tick_params(labelbottom=True, labelleft=True)

    return ax

def draw_half_court(ax=None, color='black', lw=2, outer_lines=False):
        # If an axes object isn't provided to plot onto, just get current one
        if ax is None:
            ax = plt.gca()

        backboard1 = Rectangle((50, 225), -1, 50, linewidth=lw, color=color)

        hoop1 = Circle((55, 250), radius=6, linewidth=lw, color=color, fill=False)

        restricted1 = Arc((50, 250), 80, 80, angle=270, theta1=0, theta2=180, linewidth=lw,
                         color=color)

        freethrow1_outer = Arc((195, 250), 100, 120, angle=270, theta1=0, theta2=180, linewidth=lw,
                         color=color)

        freethrow1_inner = Arc((195, 250), 100, 120, angle=270, theta1=180, theta2=0, linewidth=lw,
                         color=color, linestyle='dashed')

        freethrow1_point = Circle((195, 250), radius=4, linewidth=lw, color=color, fill=True)

        threepoint1 = Arc((90, 250), 450, 400, angle=270, theta1=0, theta2=180, linewidth=lw,
                         color=color)

        innerbox1 = Rectangle((20, 200), 175, 100, linewidth=lw, color=color,
                              fill=False)

        outbox1 = Rectangle((20, 190), 175, 120, linewidth=lw, color=color,
                          fill=False)

        half_court_circle  = Arc((490, 250), 100, 120, angle=270, theta1=180, theta2=0, linewidth=lw,
                         color=color)

        half_court_point  = Arc((490, 250), 5, 5, angle=270, theta1=180, theta2=0, linewidth=6,
                     color=color)

        lower_three_line = Rectangle((20, 25), 70, 1, linewidth=0.25*lw, color=color,
                              fill=True)

        upper_three_line = Rectangle((20, 475), 70, 1, linewidth=0.25*lw, color=color,
                          fill=True)

        # List of the court elements to be plotted onto the axes
        court_elements = [backboard1, hoop1, restricted1,
                           threepoint1, innerbox1, freethrow1_outer,freethrow1_point,
                          outbox1, freethrow1_inner,lower_three_line, upper_three_line, half_court_circle, half_court_point]

        if outer_lines:
        # Draw the half court line, baseline and side out bound lines
            outer_lines = Rectangle((20, 0), 470, 500, linewidth=lw,
                                    color=color, fill=False)
            court_elements.append(outer_lines)

          # Add the court elements onto the axes
        for element in court_elements:
            ax.add_patch(element)

        ax.set_aspect('auto')
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.tick_params(labelbottom=True, labelleft=True)
		#ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
		
        return ax
