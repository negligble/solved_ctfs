#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

	char target[] = "1_n3}f3br9Ty{_6_rHnf01fg_14rlbtB60tuarun0c_tr1y3";
	int seed = 0x13377331;

	int flagLength = strlen(target);
	int randomValues[flagLength];

	for (int i = 0; i < flagLength; i++){
		randomValues[i] = rand_r(&seed);
	}

	for (int i = flagLength - 1; i >= 0; i--) {
	        int calculatedIndex = (int)((unsigned long)(long)randomValues[i] % (flagLength - i)) + i;

        	char c = target[calculatedIndex];
        	target[calculatedIndex] = target[i];
        	target[i] = c;
	    }
	printf("%s", target);
}
