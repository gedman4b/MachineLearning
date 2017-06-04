@mfunction("h, display_array")
def displayData(X=None, example_width=None):
    # DISPLAYDATA Display 2D data in a nice grid
    # [h, display_array] = DISPLAYDATA(X, example_width) displays 2D data
    # stored in X in a nice grid. It returns the figure handle h and the 
    # displayed array if requested.

    # Set example_width automatically if not passed in
    if not exist(mstring('example_width'), mstring('var')) or isempty(example_width):
        example_width = round(sqrt(size(X, 2)))
    end

    # Gray Image
    colormap(gray)

    # Compute rows, cols
    [m, n] = size(X)
    example_height = (n / example_width)

    # Compute number of items to display
    display_rows = floor(sqrt(m))
    display_cols = ceil(m / display_rows)

    # Between images padding
    pad = 1

    # Setup blank display
    display_array = -ones(pad + display_rows * (example_height + pad), pad + display_cols * (example_width + pad))

    # Copy each example into a patch on the display array
    curr_ex = 1
    for j in mslice[1:display_rows]:
      for i in mslice[1:display_cols]:
        if curr_ex > m:
           break
        end
        # Copy the patch

        # Get the max value of the patch
        max_val = max(abs(X(curr_ex, mslice[:])))
        display_array(pad + (j - 1) * (example_height + pad) + (mslice[1:example_height]), pad + (i - 1) * (example_width + pad) + (mslice[1:example_width])).lvalue = reshape(X(curr_ex, mslice[:]), example_height, example_width) / max_val
        curr_ex = curr_ex + 1
      end
      if curr_ex > m:
         break
      end
    end

    # Display Image
    h = imagesc(display_array, mcat([-1, 1]))

    # Do not show axis
    axis(mstring('image'), mstring('off'))

    drawnow()

end
