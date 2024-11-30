import { Component } from '@angular/core';
import { LogoComponent } from '../../shared/components/logo-component/logo-component.component';
import { SearchbarComponent } from '../../shared/components/searchbar/searchbar.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [LogoComponent, SearchbarComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {

}
