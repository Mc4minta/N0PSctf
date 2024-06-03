#!/bin/bash

echo "if (sVar24 == 0x17 && ((((((((((((((((((((((cVar2 == '0' && cVar1 == 'N') && cVar3 == 'P') && cVar4 == 'S') && cVar5 == '{') && cVar6 == 'c') && cVar7 == 'H') && cVar8 == '4') && cVar9 == 'r') && cVar10 == '_') && cVar11 == '1') && cVar12 == 's') && cVar13 == '_') && cVar14 == '8') && cVar15 == 'b') && cVar16 == 'i') && cVar17 == 't') && cVar18 == 's') && cVar19 == '_') && cVar20 == '1') && cVar21 == 'N') && cVar22 == 't') && cVar23 == '}'))" | grep -o "cVar[0-9]* == '[^']'" | awk -F "'" '{print $2}' | tr -d "\n" | sed 's/0NPS/N0PS/' > flag.txt
cat flag.txt
