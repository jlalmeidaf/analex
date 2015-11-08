package compilador;

import java.util.ArrayList;
import java.util.Stack;

public class Token {
   String[] keywords  = {"program", "var", "end;","begin", "loop","goto","<-","+"}; 
   String[][] identifiers;
   Stack stack = new Stack();
}
