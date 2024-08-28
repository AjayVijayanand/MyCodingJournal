#include <stdio.h>

int main(void)
{
  printf("(a) Printing the integer 15 using various conversion specifiers\n\n");
  printf("Recap: %%m means minimum width of m spaces\n\n");
  printf("Conversion Specifier      Display\n");
  printf("-----------------------------------\n");
  printf("         %%d               %d\n", 15);
  printf("         %%5d              %5d(There are 3 spaces before the number)\n", 15);
  printf("         %%-5d             %-5d(There are 3 spaces after the number\n", 15);
  printf("                                because of negative sign, i.e. %%-m)\n");
  printf("         %%1d              %1d\n", 15);
  printf("-----------------------------------\n\n");

  printf("Printing 7 using %%c gives %c\n", 7);
  printf("Heard the beep?\n\n");

  printf("Printing 65 using %%c gives %c\n", 65);
  printf("Printing 32 using %%c gives %c (Is any character displayed?)\n", 32);
  printf("Printing 48 using %%c gives %c\n", 48);
  printf("===============================================================\n\n");

  printf("(b) Printing the real number 12.34567 \n\n");
  printf("Recap: %%m.n means minimum width of m spaces with n number of decimal places\n\n");
  printf("Conversion Specifier      Display\n");
  printf("----------------------------------------\n");
  printf("        %%f                %f\n", 12.34567);
  printf("        %%e                %e\n", 12.34567);
  printf("        %%E                %E\n", 12.34567);
  printf("        %%10.3f            %10.3f\n", 12.34567);
  printf("        %%10.3E            %10.3E\n", 12.34567);
  printf("        %%.8f              %.8f\n", 12.34567);
  printf("----------------------------------------\n\n\n");


  printf("(c) Printing the real number 0.0000123456789\n\n");
  printf("Conversion Specifier      Display\n");
  printf("----------------------------------------\n");
  printf("        %%f                %f\n", 0.0000123456789);
  printf("        %%e                %e\n", 0.0000123456789);
  printf("        %%E                %E\n", 0.0000123456789);
  printf("        %%8.3f             %8.3f\n", 0.0000123456789);
  printf("        %%8.3e             %8.3e\n", 0.0000123456789);
  printf("        %%12.7f            %12.7f\n", 0.0000123456789);
  printf("        %%12.3f            %12.3f\n", 0.0000123456789);
  printf("        %%.3f              %.3f\n", 0.0000123456789);
  printf("        %%1.7f             %1.7f\n", 0.0000123456789);
  printf("        %%5.7f             %5.7f\n", 0.0000123456789);
  printf("===============================================================\n\n\n\n");

  return 0;
}