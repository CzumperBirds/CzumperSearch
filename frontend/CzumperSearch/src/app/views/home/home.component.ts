import { Component, OnDestroy, OnInit } from '@angular/core';
import { LogoComponent } from '../../shared/components/logo-component/logo-component.component';
import { SearchbarComponent } from '../../shared/components/searchbar/searchbar.component';
import { SearchingService } from '../../shared/services/searching.service';
import { DataContainerComponent } from '../../shared/components/data-container/data-container.component';
import { CommonModule } from '@angular/common';
import { DataInstance } from '../../shared/interfaces/dataInstance.model';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [LogoComponent, SearchbarComponent, DataContainerComponent, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit, OnDestroy{

  data : Array<DataInstance> = [];
  private dataSubscription: Subscription | undefined;

  constructor (private searchService: SearchingService){
  }

  ngOnInit(): void {
    this.dataSubscription = this.searchService.bindDataSet().subscribe((data) => {
      this.data = data;
    });
  }

  ngOnDestroy(): void {
    if (this.dataSubscription) {
      this.dataSubscription.unsubscribe();
    }
  }

}
