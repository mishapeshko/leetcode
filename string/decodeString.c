#include <ctype.h>

#define MAX_N 31
#define MAX_L 10001

typedef struct StackInt{
    int start;
    int end;
    int* values;
} StackInt;

typedef struct StackChar{
    int start;
    int end;
    char** values;
} StackChar;

int popInt(StackInt* stackInt){
    int item = stackInt->values[--stackInt->end];
    if(stackInt->end == stackInt->start){
        stackInt->end = 0;
        stackInt->start = -1;
    }
    return item;
}

char* popChar(StackChar* stackChar){
    char* item = stackChar->values[--stackChar->end];
    if(stackChar->end == stackChar->start){
        stackChar->end = 0;
        stackChar->start = -1;
    }
    return item;
}

void pushInt(StackInt* stackInt, int value){
    if(stackInt->start == -1) stackInt->start = 0;
    stackInt->values[stackInt->end++] = value;
}

void pushCharP(StackChar* stackChar, char* value){
    if(stackChar->start == -1) stackChar->start = 0;
    stackChar->values[stackChar->end++] = value;
}

int isEmptyInt(StackInt* stackInt){
    return stackInt->start == -1;
}

int isEmptyCharP(StackChar* stackChar){
    return stackChar->start == -1;
}

char* decodeString(char* s) {
    int balans = 0;
    StackInt* stackInt = (StackInt*)malloc(sizeof(StackInt));
    stackInt->start = -1;
    stackInt->end = 0;
    stackInt->values = (int*)malloc(sizeof(int)*MAX_N);
    StackChar* stackChar = (StackChar*)malloc(sizeof(StackChar));
    stackChar->start = -1;
    stackChar->end = 0;
    stackChar->values = (char**)malloc(sizeof(char)*MAX_L);
    int i = 0;
    char* res = (char*)malloc(sizeof(char)*MAX_L);
    int idx_res = 0;
    while(s[i] != '\0'){
        if(isdigit(s[i])){
            int number = 0;
            while(isdigit(s[i])){
                number *= 10;
                number += s[i]-'0';
                i++;
            }
            pushInt(stackInt, number);
        }
        else{
            if(s[i] == '['){
                balans++;
                i++;
                int j = i;
                int len = 0;
                while(isalpha(s[j])){
                    j++;
                    len++;
                }
                char* curr = (char*)malloc(sizeof(char)*(len+1));
                int idx = 0;
                while(isalpha(s[i])){
                    curr[idx++] = s[i];
                    i++;
                }
                curr[len] = '\0';
                pushCharP(stackChar, curr);
            }
            else if(s[i] == ']'){
                balans--;
                int howM = popInt(stackInt);
                char* str = popChar(stackChar);
                int len = 0;
                while(str[len] != '\0'){
                    len++;
                }
                char* newStr = (char*)malloc(sizeof(char)*(howM*len));
                for(int k = 0; k < howM*len; k++){
                    newStr[k] = str[k%len];
                }
                if(balans == 0){
                    for(int o = 0; o < howM*len; o++){
                        res[idx_res++] = newStr[o];
                    }
                }
                else{
                    char* topC = popChar(stackChar);
                    int lenTopC = 0;
                    while(topC[lenTopC] != '\0'){
                        lenTopC++;
                    }
                    int newL = lenTopC+len*howM;
                    char* finalC = (char*)malloc(sizeof(char)*(newL+1));
                    int final_idx = 0;
                    for(int j = 0; j < lenTopC; j++){
                        finalC[final_idx++] = topC[j];
                    }   
                    for(int u = 0; u < len*howM; u++){
                        finalC[final_idx++] = newStr[u];
                    }
                    finalC[newL] = '\0';
                    free(topC);
                    pushCharP(stackChar, finalC);
                }
                free(newStr);
                free(str);
                i++;
            }
            else{
                if(balans == 0){
                    while(isalpha(s[i])){
                        res[idx_res++] = s[i++];
                    }
                }
                else{
                    char* topC = popChar(stackChar);
                    int lenTopC = 0;
                    while(topC[lenTopC] != '\0'){
                        lenTopC++;
                    }
                    int lenCharP = 0;
                    int j = i;
                    while(isalpha(s[j])){
                        j++;
                        lenCharP++;
                    }
                    char* betCharP = (char*)malloc(sizeof(char)*lenCharP);
                    int charP_idx = 0;
                    while(isalpha(s[i])){
                        betCharP[charP_idx++] = s[i++];
                    }
                    int newL = lenCharP+lenTopC;
                    char* helpChar = (char*)malloc(sizeof(char)*(newL+1));
                    int help_idx = 0;
                    for(int t = 0; t < lenTopC; t++){
                        helpChar[help_idx++] = topC[t];
                    }
                    for(int t = 0; t < lenCharP; t++){
                        helpChar[help_idx++] = betCharP[t];
                    }
                    helpChar[newL] = '\0';
                    pushCharP(stackChar, helpChar);
                }
            }
        }
    }
    res[idx_res] = '\0';
    return res;
}
