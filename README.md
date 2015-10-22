# Analex

O análisador léxico para a linguagem de programação minimal (LPM), desenvolvido pela turma de compiladores do curso de ciência da computação da Universidade Estadual do Norte Fluminense no segundo semestre de 2015.

## Linguagem LPM

LPM é uma linguagem bastante semelhante com os primórdios da linguagem Fortran.  Além disto, LPM possui um conjunto de regras que são usadas em outras linguagens imperativas (Lins et al. XXXX).

### Comandos possíveis:

z <- 0;
z <- z+1;
loop z;
z <- x;
goto l1;
end;

### Exemplo de programa em LPM:

program hello

var
	x:integer, y:integer;

end;

begin

	x <- 0;

	x <- x + 1;

 L1 y <- 0;

	loop x;

		y <- y+1;

		goto L1;

	end;

end;
	

 

## Objetivo

O objetivo deste projeto é desenvolver um analisador léxico para a linguagem LPM usando o conteúdo discutido em sala de aula. Qualquer dúvida enviar um e-mail para mim: joaoluiz.af@gmail.com
