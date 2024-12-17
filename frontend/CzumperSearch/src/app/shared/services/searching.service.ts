import { Injectable } from '@angular/core';
import { DataInstance } from '../interfaces/dataInstance.model';
import { BehaviorSubject } from 'rxjs';
import { Observable } from 'rxjs';
import { pickupLines } from '../mocks/mockedJokes';
@Injectable({
  providedIn: 'root'
})
export class SearchingService {

  getMockData() {
    return pickupLines
  }

  private foundData : BehaviorSubject<Array<DataInstance>> = new BehaviorSubject<Array<DataInstance>>([ {
    type: "joke",
    source: "Google",
    content: "Jesteś może małym AGD? Bo kręcisz mnie jak mikrofalówka talerz.",
    published: "28.07.1742 21:37:00",
    tags: ["Dark","Nose","AgataMeble","EightStars"]
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
          this.foundData.next(this.getMockData());
          resolve("Operation was successful!");
        } else {
          reject("Something went wrong!");
        }
      }, 2000);
    });
  }
}
