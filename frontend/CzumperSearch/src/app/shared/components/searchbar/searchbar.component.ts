import { Component } from '@angular/core';
import { SearchingService } from '../../services/searching.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-searchbar',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './searchbar.component.html',
  styleUrl: './searchbar.component.scss'
})
export class SearchbarComponent {

  constructor (private searchService : SearchingService){

  }

  searchString : string = ''

  async searchForData(){
    this.searchService.searchData(this.searchString)
  }

}
