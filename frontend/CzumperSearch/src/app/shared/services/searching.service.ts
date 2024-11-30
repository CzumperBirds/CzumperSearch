import { Injectable } from '@angular/core';
import { DataInstance } from '../interfaces/dataInstance.model';
import { BehaviorSubject } from 'rxjs';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SearchingService {

  private foundData : BehaviorSubject<Array<DataInstance>> = new BehaviorSubject<Array<DataInstance>>([ {
    title: "Piwo",
    content: "Lubię piwo",
    type: "fact"
  }]);

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
              title: "Piwo",
              content: "Lubię piwo",
              type: "fact"
            },
            {
              title: "Nos kacpra",
              content: "Kacper nie ma długiego nosa",
              type: "joke"
            },
            {
              title: "Nos Kacpra",
              content: "Kacper ma długi nos",
              type: "fact"
            },
            {
              title: "Komputer Artura",
              content: "Ten serwis będzie działał do momentu w którym zacznie padać śnieg",
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
