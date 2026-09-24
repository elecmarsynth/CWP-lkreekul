def checkmate (board) :
      grid = board.strip().split('\n')
      size = len(grid)

      k_row, k_col = -1,-1

      for i in range(size) :
            for j in range(size):
                  if grid[i][j] == 'K' :
                        k_row = i
                        k_col = j
                        break
            if k_row != -1 :
                  break

      if k_row == -1 :
            print("not found king")
            return


      coord = [
            (-1,0), (1,0), (0,-1), (0,1),
            (-1,-1), (-1,1), (1,-1), (1,1)
      ]

      for direct_r, direct_c in coord :
            r = k_row + direct_r
            c = k_col +  direct_c

            while 0 <= r < size and 0 <= c < size :
                  current_noww = grid[r][c]

                  if current_noww != '.' :
                        if direct_r == 0 or direct_c == 0 :
                              if current_noww in ('R', 'Q') :
                                    print("Success")
                                    return
                        else :
                              if current_noww in ('B', 'Q') :
                                    print("Success")
                                    return

                        break

                  r += direct_r
                  c += direct_c

      pawnCoord = (
            (k_row + 1, k_col - 1),
            (k_row + 1, k_col + 1)
      )

      for r_p, c_p in pawnCoord :
            if 0 <= r_p < size or 0 <= c_p < size :
                  if (grid[r_p][c_p] == "P") :
                        print("Success")
                        return

      print("Fail")