package dndLogic;

import org.eclipse.jface.viewers.ILabelProviderListener;
import org.eclipse.jface.viewers.ITableLabelProvider;
import org.eclipse.swt.graphics.Image;

import dndCharacter.CharInfo;

public class CharLabelProvider implements  ITableLabelProvider {

	@Override
	public void addListener(ILabelProviderListener arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void dispose() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public boolean isLabelProperty(Object arg0, String arg1) {
		// TODO Auto-generated method stub
		return true;
	}

	@Override
	public void removeListener(ILabelProviderListener arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public Image getColumnImage(Object arg0, int arg1) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String getColumnText(Object arg0, int arg1) {
		CharInfo charInfo = (CharInfo) arg0;
		switch (arg1) {
		case 0: {			
			return charInfo.getName();
		}
		case 1: {			
			return String.valueOf(charInfo.getInit());
		}
		case 2: {			
			return String.valueOf(charInfo.getMaxHP());
		}
		case 3: {			
			return String.valueOf(charInfo.getCurrentHP());
		}
		
		
	}
	
		return "";

	}
}