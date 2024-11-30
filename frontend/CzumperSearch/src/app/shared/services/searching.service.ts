import { Injectable } from '@angular/core';
import { DataInstance } from '../interfaces/dataInstance.model';
import { BehaviorSubject } from 'rxjs';  // Import BehaviorSubject
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SearchingService {

  private foundData : BehaviorSubject<Array<DataInstance>> = new BehaviorSubject<Array<DataInstance>>([]);

  constructor() {
  }

  bindDataSet(): Observable<Array<DataInstance>> {
    return this.foundData.asObservable();
  }

  searchData() : Promise<unknown>{
    console.log('Searching for data')
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        const success = true;
        if (success) {
          this.foundData.next([
            {
              title: "fact",
              content: "fact",
              type: "fact"
            },
            {
              title: "joke",
              content: "joke",
              type: "joke"
            },
            {
              title: "fact",
              content: "fact",
              type: "fact"
            },
            {
              title: "fact",
              content: "fact",
              type: "fact"
            }
          ]);
          resolve("Operation was successful!");
        } else {
          reject("Something went wrong!");
        }
      }, 2000);
    });
  }
}
