use strict;
use warnings;
# This helps you find typing mistakes, it warns you whenever it sees something wrong with your program

my $s;          #stores the alphabets which can be used in the generation of the random string
my $file;       #stores the name of the input file
print "Please enter the required file 🙏:\n";
$file = <STDIN>; #taking input
chomp($file);    #chomping \n

#while loop to read the input from the input file
open my $info, $file or die "Could not open $file: $!";
while( my $line = <$info>)  {   
    $s = $line;    
    chomp($s);
    last if $. == 2;
}
close $info;

my $cnt; #stores the maximum count of an alphabet
print "Please enter the required count-number 🙏:\n";
$cnt = <STDIN>;

my $length; #stores the length of the string
print "Please enter the required length of string 🙏:\n";
$length = <STDIN>;

my $n = length($s);
my $index = int rand($n);       #randomly selected index whose alphabet to be printed 
my $c = '.';                    #retrieving the alphabet to be printed from the index
my $consec = 1;                 #keeps the number of consecutive occurences of an alphabet

if($cnt <= 1){print "Error: The count has to be greater than or equal to 2. This value of count will produce undefined behaviour. \n"}
#for loop to print the rest of the string
print "The randomly generated string is: ";
for(my $i = 0; $i<$length; $i++)
{
    $index = int rand($n);
    #case 1: if the number of consecutive occurences is less than cnt -> print the alphabet
    if($c eq substr($s, $index, 1) && ($consec + 1 < $cnt))
    {
        print $c; 
        $consec = $consec + 1;
    }
    #case 2: if the number of consecutive occurences is equal to cnt -> print the some another alphabet
    elsif($c eq substr($s, $index, 1))
    {
        while($c eq substr($s, $index, 1)){$index = int rand($n);}
        $c = substr($s, $index, 1);
        print $c;
        $consec = 1;
    }
    #case 3: the character is different from the previous character -> print the character
    elsif($consec + 1 < $cnt)
    { 
        $c = substr($s, $index, 1);
        print $c;
        $consec = 1;
    }
}
print " 😀\n";