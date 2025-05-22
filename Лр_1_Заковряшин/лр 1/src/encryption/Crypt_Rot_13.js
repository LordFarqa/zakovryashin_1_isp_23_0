import { RotIndex, LatAlphavit, LatAlphavitBig } from "../config/config.js";

export function Crypt(Array) {
    let ResArr = [];
    for (let i = 0; i < Array.length; i++) {
        var flag = true
        for (let j = 0; j < LatAlphavit.length; j++) {
            if (LatAlphavit[j] === Array[i]) {
                if (j >= RotIndex) {
                    ResArr.push(LatAlphavit[j - RotIndex]);
                } else {
                    ResArr.push(LatAlphavit[j + RotIndex]);
                }
                var flag = false
            }
            if (LatAlphavitBig[j] === Array[i]) {
                if (j >= RotIndex) {
                    ResArr.push(LatAlphavitBig[j - RotIndex]);
                } else {
                    ResArr.push(LatAlphavitBig[j + RotIndex]);
                }
                var flag = false
            }
        }
        if(flag){
            ResArr.push(Array[i]);
        }
    }
    return ResArr;
}
