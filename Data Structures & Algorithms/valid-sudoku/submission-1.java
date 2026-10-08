class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, Integer> rows = new HashMap<>(); 
        HashMap<Integer, Integer> columns = new HashMap<>();
        HashMap<Integer, Integer> squares = new HashMap<>();

        //check rows
        for(int i=0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                if(board[i][j] != '.'){
                    int parsed = Integer.parseInt(String.valueOf(board[i][j]));
                    System.out.println(parsed);
                    if(rows.get(parsed)!=null && rows.get(parsed)==i){
                        System.out.println("rows fail");
                        return false;
                    }
                    rows.put(parsed, i);
                }
            }

        }
        //check columns
        for(int i=0; i<board[0].length; i++){
            for(int j = 0; j<board.length; j++){
                if(board[j][i] != '.'){
                    int parsed = Integer.parseInt(String.valueOf(board[j][i]));
                    if(columns.get(parsed)!=null && columns.get(parsed)==i){
                        System.out.println("columns fail");
                        return false;
                    }
                    columns.put(parsed, i);
                }
            }
        }
        //check squares
        for(int i=0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                if(board[i][j] != '.'){
                    int squareIndex = (i/3)*3 + (j/3);
                    int parsed = Integer.parseInt(String.valueOf(board[i][j]));
                    if(squares.get(parsed)!=null && squares.get(parsed)==squareIndex){
                        System.out.println(parsed);
                        return false;
                    }
                    squares.put(parsed, squareIndex);
                }
            }
        }
        return true;
    }
}
