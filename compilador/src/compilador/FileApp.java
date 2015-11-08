package compilador;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FileApp {

	public void readerFile() {
		try {
			FileReader arq = new FileReader("/home/rodolfopeixoto/workspace/compilador/src/compilador/codigo.txt");
			BufferedReader readArq = new BufferedReader(arq);
			String line = readArq.readLine(); // reads the first line
			ArrayList<String> lineBreak = new ArrayList();

			while (line != null) {

				lineBreak.add(line);

				line = readArq.readLine();

			}

			arq.close();

			Lexical l = new Lexical();
			Token t = new Token();
			String[] characters;

			for (int i = 0; i < lineBreak.size(); i++) {
				l.analysis(lineBreak.get(i));
				characters = lineBreak.get(i).split(" ");

				for (int j = 0; j < characters.length; j++) {
					switch (characters[j]) {
					case "program":
						Pattern nameProgramregex = Pattern.compile("(s?)program.*[;]");
						Matcher matcProgramRegex = nameProgramregex.matcher(lineBreak.get(i));
						if (matcProgramRegex.find()) {
							t.stack.push(characters[j]);
							characters[j + 1] = characters[j + 1].replace(";", "");
							t.stack.push(characters[j + 1]);

						}
						break;

					default:
						break;
					}
				}
				
				
			
				

			}
		

			// line = readArq.readLine(); // reads the first line

			// System.out.println(" line " + line);

		} catch (Exception e) {
			System.err.printf("Error na abertura do arquivo: %s\n", e.getMessage());
		}

	}

}
