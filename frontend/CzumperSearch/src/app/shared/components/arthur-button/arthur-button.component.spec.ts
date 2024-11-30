import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArthurButtonComponent } from './arthur-button.component';

describe('ArthurButtonComponent', () => {
  let component: ArthurButtonComponent;
  let fixture: ComponentFixture<ArthurButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ArthurButtonComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ArthurButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
