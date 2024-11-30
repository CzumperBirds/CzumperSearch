import { Component } from '@angular/core';
import { SearchingService } from '../../services/searching.service';

@Component({
  selector: 'app-searchbar',
  standalone: true,
  imports: [],
  templateUrl: './searchbar.component.html',
  styleUrl: './searchbar.component.scss'
})
export class SearchbarComponent {

  constructor (private searchService : SearchingService){

  }

  async searchForData(){
    this.searchService.searchData()
    console.log("Data found")
  }

}
